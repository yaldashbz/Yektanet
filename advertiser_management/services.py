def update_all_advertisers(advertisers):
    for advertiser in advertisers:
        if len(advertiser.ads.all()) == 0:
            advertiser.update_empty_on_view()
        else:
            for ad in advertiser.ads.all():
                ad.update_on_view()
