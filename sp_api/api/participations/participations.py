import urllib

from sp_api.base import Client, Marketplaces, sp_endpoint, ApiResponse


class Participations(Client):
    """
    :link: https://developer-docs.amazon.com/sp-api/docs/sellers-api-v1-reference#get-sellersv1marketplaceparticipations
    """

    @sp_endpoint('/sellers/v1/marketplaceParticipations')
    def get_marketplace_participations(self, **kwargs) -> ApiResponse:
        """
        get_marketplace_participations(self, **kwargs) -> GetMarketplaceParticipationsResponse


        Returns a list of marketplaces that the seller submitting the request can sell in and information about the seller's participation in those marketplaces.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        .016                                     15
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Usage Plan:

        Args:
            N/A

        Returns:
            GetMarketplaceParticipationsResponse:

        """

        return self._request(kwargs.pop('path'), params=kwargs)
