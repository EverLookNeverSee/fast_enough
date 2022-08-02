from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def hello_world(self):
        self.client.get('/')

    data = [
        {'id': 1, 'item': 'Buy milk', 'status': 'pending'},
        {'id': 2, 'item': 'Read car', 'status': 'pending'},
        {'id': 3, 'item': 'Buy eggs', 'status': 'pending'},
        {'id': 4, 'item': 'Buy bread', 'status': 'pending'},
        {'id': 5, 'item': 'Buy cheese', 'status': 'pending'},
        {'id': 6, 'item': 'Buy pen', 'status': 'pending'},
        {'id': 7, 'item': 'buy pencil', 'status': 'pending'},
        {'id': 8, 'item': 'Buy shirt', 'status': 'pending'},
        {'id': 9, 'item': 'go shopping', 'status': 'pending'},
        {'id': 10, 'item': 'go swimming', 'status': 'pending'},
    ]

    @task(10)
    def add_todo(self):
        for item in self.data:
            self.client.post('/todo', json=item)

    @task(9)
    def retrieve_todos(self):
        self.client.get('/todo')

    @task(8)
    def get_single_todo(self):
        for item in self.data:
            self.client.get('/todo/{}'.format(item['id']))

    @task(7)
    def update_todo(self):
        for item in self.data:
            self.client.put('/todo/{}'.format(item['id']), json=item)

    @task(5)
    def delete_single_todo(self):
        for item in self.data:
            self.client.delete('/todo/{}'.format(item['id']))

    @task(2)
    def delete_all_todos(self):
        self.client.delete('/todo')
