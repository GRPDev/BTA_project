from FileManager import FileManager
from HistoryMessages import HistoryMessages
import request

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
        self.file_manager.add_to_json(hist_dict, self.hist_file_path) 

    def get_exchange_rates(self):
        # Implement a process that sends a get request to the link 
        # and returns the resulting dictionary.
        try:
            exc_rates = requests.get("https://fake-api.apps.berlintech.ai/api/currency_exchange")
            if exc_rates.status_code == 200:
                return exc_rates.json()
        except Exception:
            raise Exception("Something went wrong")
        
    def exchange_currency(self, currency_from, currency_to, amount):
        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency
        
        rates = self.get_exchange_rates() #json.loads(exc_rates.text)
        try:
            amount = float(amount)
        except Exception:
            print('Currency exchange failed!')
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None
        
        if amount <= 0:
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            print("Currency exchange failed!")
            
        elif currency_from not in rates or currency_to not in rates:
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            print("Currency exchange failed!")

        elif currency_from == "EUR":    #exchange EUR to any currency
            converted_amount = rates[currency_to] * amount
            history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
            self.write_to_history(history_message)
            return converted_amount
                        
        elif currency_from != "EUR" and currency_to == "EUR":   #exchange any currency to EUR
            converted_amount = amount / rates[currency_from]
            history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
            self.write_to_history(history_message)
            return converted_amount
                
        elif currency_from != "EUR" and currency_to != "EUR":   #exchange any currency to any currency
            temp_conversion = amount / rates[currency_from]     #convert any currency to EUR
            converted_amount = rates[currency_to] * temp_conversion   #convert EUR to any currency
            history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
            self.write_to_history(history_message)
            return converted_amount