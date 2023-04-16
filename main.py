import requests
import string
import random
class Check:
    codes = []
    @staticmethod
    def gen():
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(19))
    @staticmethod
    async def check():
        check = Check.gen()
        Check.codes.append(check)
        try:
            response = requests.get(f"https://discord.com/api/v7/entitlements/gift-codes/{check}?with_application=false&with_subscription_plan=true")
            response.raise_for_status()
            data = response.json()
            if data["message"] == "Unknown Gift Code":
	            print(f"Not Working: https://discord.gift/{check}")
            else:
                print(f"🎉 Possibly Working: https://discord.gift/{check}")
                with open("workedcodes.txt", "a+") as f:
                    f.write(f"\n{check}")
        except requests.exceptions.HTTPError as error:
            print(f"❌ HTTP Error: {error}")
        except requests.exceptions.ConnectionError as error:
            print(f"❌ Connection Error: {error}")
        except requests.exceptions.Timeout as error:
            print(f"❌ Timeout Error: {error}")
        except requests.exceptions.RequestException as error:
            print(f"❌ Unexpected Error: {error}")
Check()
