import unittest
from credit_card import *


class CreditCardTests(unittest.TestCase):

	def setUp(self):
		self.func_1 = CreditCard("Amex", "2345673444", "12/15", "2345", [234, 567, 456, 567, 344])
		self.func_2 = CreditCard("Bancomer", "2345673444", "12/15", "2645", [234, 345, 456, 567, 344])

	def test_name_is_evaluated_as_getter(self):
	    self.assertEqual(self.func_1.name, "Amex")

	def test_name_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func_1.name = "Amex to Go"

	def test_number_is_evaluated_as_getter(self):
	    self.assertEqual(self.func_1.number, "2345673444")

	def test_number_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func_1.number = "2345677447"

	def test_expiration_is_evaluated_as_getter(self):
	    self.assertEqual(self.func_1.expiration, "12/15")

	def test_expiration_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func_1.expiration = "12/23"

	def test_cvc_is_evaluated_as_getter(self):
	    self.assertEqual(self.func_1.cvc, "2345")

	def test_expiration_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func_1.cvc = "2347"

	def test_status_is_evaluated_as_getter(self):
	    self.assertEqual(self.func_1.status, [234, 567, 456, 567, 344])

	def test_status_is_evaluated_as_setter(self):
	    raised = False
	    try:
	    	self.func_1 = [234, 567, 456, 567, 980]
	    except:
	    	raised = True
	    self.assertFalse(raised, "Exception raised")

	def test_total_status_returns_total_of_balances_of_creditcard(self):
		self.assertEqual(self.func_2.total_status(), 1946)


class PortfolioTests(unittest.TestCase):

	def setUp(self):
		self.func_amex = CreditCard("Amex", "2345673444", "12/15", "2345", [234, 567, 456, 567, 344])
		self.func_bancomer = CreditCard("Bancomer", "2345673444", "12/15", "2645", [234, 345, 456, 567, 344])
		self.func_scotiabank = CreditCard("ScotiaBank", "2345673744", "12/16", "2845", [234, 345, 456, 567, 344])
		self.func_serfin = CreditCard("Serfin", "2345473454", "12/20", "1345", [234, 345, 456, 567, 344])
		self.func_bancoppel = CreditCard("BanCoppel", "2345373464", "12/18", "2445", [567, 345, 456, 567, 344])
		self.func_banregio = CreditCard("BanRegio", "2345373464", "12/18", "2445", [567, 345, 456, 567, 344])
		self.func_portfolio = Portfolio([self.func_amex, self.func_scotiabank, self.func_bancomer, self.func_serfin, self.func_bancoppel])

	def test_how_many_cards_if_how_many_cards_returns_total_of_creditcards_in_portfolio(self):
		self.assertEqual(self.func_portfolio.how_many_cards(), 5)

	def test_add_creditcard_if_add_creditcard_adds_a_new_creditcard_in_portfolio(self):
		raised = False
		try:
			self.func_portfolio.add_creditcard(self.func_banregio)
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")
		self.assertEqual(self.func_portfolio.how_many_cards(), 6)

	def test_sum_portfolio_if_sum_portfolio_returns_total_balances_of_portfolio(self):
		self.func_portfolio.add_creditcard(self.func_banregio)
		self.assertEqual(self.func_portfolio.sum_portfolio(), 12564)

	def test_delete_creditcard_if_delete_creditcard_drops_a_creditcard_from_portfolio(self):
		self.func_portfolio.add_creditcard(self.func_banregio)
		raised = False
		try:
			self.func_portfolio.delete_creditcard("Bancomer")
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")
		self.assertEqual(self.func_portfolio.how_many_cards(), 5)
		self.assertEqual(self.func_portfolio.sum_portfolio(), 10618)


if __name__=="__main__":
    unittest.main()