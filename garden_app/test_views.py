from django.test import TestCase, Client
from garden_project.factories import UserFactory, TemperatureFactory, SoilMoistureFactory


class TestGardenViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        temp = TemperatureFactory(user=self.user)
        soil = SoilMoistureFactory()
        res = self.c.get('')

        self.assertIn(temp.temperature.encode(), res.content)
        self.assertIn(soil.has_moisture, True)

    # def test_lists_only_owned_budgets(self):
    #     self.c.login(
    #         username=self.user.username,
    #         password='secret'
    #     )

    #     own_budget = BudgetFactory(user=self.user)
    #     other_budget = BudgetFactory()

    #     res = self.c.get('/budgets')

    #     self.assertIn(own_budget.name.encode(), res.content)
    #     self.assertNotIn(other_budget.name.encode(), res.content)

    # def test_budgets_listed_in_view(self):
    #     self.c.login(
    #         username=self.user.username,
    #         password='secret'
    #     )
    #     budget = BudgetFactory(user=self.user)
    #     transaction = TransactionFactory(budget=budget)
    #     res = self.c.get('/budgets')
    #     self.assertIn(budget.name.encode(), res.content)


# class TestBudgetCreateViews(TestCase):
#     def setUp(self):
#         self.user = UserFactory()
#         self.user.set_password('secret')
#         self.user.save()
#         self.c = Client()

#     def test_create_view_adds_new_budget(self):
#         self.c.login(
#             username=self.user.username,
#             password='secret'
#         )

#         form_data = {
#             'name': 'Budget One',
#         }

#         res = self.c.post('/budgets/add', form_data, follow=True)
#         # Confirms the record was retrieved from the database and presented in the view
#         self.assertIn(b'Budget One', res.content)


# class TestCardCreateViews(TestCase):
#     def setUp(self):
#         self.user = UserFactory()
#         self.user.set_password('secret')
#         self.user.save()

#         self.budget = BudgetFactory(name=self.user)

#         self.c = Client()

#     def test_create_view_adds_new_category(self):
#         self.c.login(
#             username=self.user.username,
#             password='secret'
#         )

#         form_data = {
#             'budget': self.budget.name,
#             'title': 'long description...',
#         }

#         res = self.c.post('/transaction/add', form_data, follow=True)

#         # Confirms the record was retrieved from the database and presented in the view
#         self.assertIn(b'long description...', res.content)


