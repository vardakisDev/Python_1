from igramscraper.instagram import Instagram

instagram =Instagram()


account = instagram.get_account('stelios_vrdks')

print(account.full_name)


comments = account.get