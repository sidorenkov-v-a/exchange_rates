from rest_framework.routers import Route, SimpleRouter


class RateRouter(SimpleRouter):
    routes = [
        Route(
            url='currencies',
            mapping={'get': 'list'},
            name='currencies-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url='currency/{lookup}',
            mapping={'get': 'retrieve'},
            name='currencies-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]
