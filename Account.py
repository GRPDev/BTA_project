from FileManager import FileManager
from HistoryMessages import HistoryMessages
import json

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        #with open(self.hist_file_path, "a") as file:
        #    json.dump(hist_dict,file)
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        self.file_manager.add_to_json(hist_dict,self.hist_file_path)

    def deposit(self, amount):
        try:
            deposit_amount = int(amount)
            if deposit_amount > 0:
                self.balance += amount
                history_message = HistoryMessages.deposit("success", amount, self.balance)
                self.write_to_history(history_message)
            elif deposit_amount <= 0:
                history_message = HistoryMessages.deposit("failure", amount, self.balance)
                self.write_to_history(history_message)
                raise ValueError("Invalid amount for deposit!")
        except Exception:
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            raise Exception("Invalid amount for deposit!")

    def debit(self, amount):
        try:
            debit_amount = int(amount)
            if debit_amount > 0 and self.balance > debit_amount:
                self.balance -= amount
                history_message = HistoryMessages.debit("success", amount, self.balance)
                self.write_to_history(history_message)
            elif debit_amount > 0 and self.balance < debit_amount:
                print("Invalid amount for debit!")
                history_message = HistoryMessages.debit("failure", amount, self.balance)
                self.write_to_history(history_message)
            elif debit_amount <= 0:
                print("Invalid amount for debit!")
                history_message = HistoryMessages.debit("failure", amount, self.balance)
                self.write_to_history(history_message)
        except Exception:
            raise Exception("Invalid amount for debit!") 

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        
    def get_history(self):
        with open(self.hist_file_path, "r") as file:
            data = json.load(file)
            for i in data:
                self.dict_to_string(i)
        # TODO:
        # implement a process that returns transaction history line by line
        # use the dict_to_string method to create a string from a dictionary