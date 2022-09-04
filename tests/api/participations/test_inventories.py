from sp_api.api import Participations
from sp_api.base import SellingApiForbiddenException


def test_get_marketplace_participations():
    res = Participations().get_marketplace_participations(**{
        "details": True,
        "marketplaceIds": ["ATVPDKIKX0DER"]
    })
    assert res.errors is None
    assert res.pagination.get('nextToken') == 'seed'
    assert res.payload.get('granularity').get(
        'granularityType') == 'Marketplace'


def test_get_marketplace_participations_expect_500():
    try:
        Participations().get_marketplace_participations(**{
            "marketplaceIds": ["1"],
        })
    except SellingApiForbiddenException as se:
        assert se.code == 403
