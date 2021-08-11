from rest_framework.routers import Route, SimpleRouter


class CurrencyRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^currencies/$',
            mapping={'get': 'list'},
            name='currencies-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'currency/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='currencies-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]
