GOING_UP = 'Elevator is going up'
GOING_DOWN = 'Elevator is going down'
STOPPED = 'Elevator stopped'

class Elevator:

    def  __init__(self):
        self.current_floor = 0
        self.is_opened = True
        self.status = STOPPED
        # list of dictionaries
        self.route = []
        self.people = 0

    def  set_route(self, route):
        ''' Add route containing the requested floor and the number of people to the same floor '''

        # search if the requested route is the same floor as the elevator.
        if self.current_floor == route:
            self.people = self.people - 1
            print ('This requested floor is the current floor')
            return
        if self.capacity_is_full():
            print('Only one route per person is allowed')
            return
        # search if the required floor is already on the route
        route_exists = [x for x in self.route if x.get('floor') == route]
        if len(route_exists) == 0:
            self.route.append(dict(floor=route, total=1))
            self.route = sorted(self.route, key=lambda k: k['floor'])
            self.is_opened = True
        else:
            print('This floor is already called')
            # adds another person on the planned route
            route_exists[0]['total'] = route_exists[0]['total'] + 1

    def  move(self):
        ''' movimenta o elevador para cima ou para baixo '''
        while len(self.route) > 0:
            self.is_opened = False
            if (self.route[0]['floor'] - self.current_floor > 0):
                move_up = range(self.current_floor, self.route[0]['floor'])
                for floor in move_up:
                    self.status = GOING_UP
                    self.current_floor = floor + 1
                    self.show_all_variables()
            else:
                move_down = range(self.current_floor, self.route[0]['floor'], -1)
                for floor in move_down:
                    self.status = GOING_DOWN
                    self.current_floor = floor - 1
                    self.show_all_variables()
            self.status = STOPPED
            self.people = self.people - self.route[0]['total']
            self.is_opened = True
            self.route.pop(0)
            self.show_all_variables()

    def  set_people(self):
        ''' add people to the elevator'''
        self.people = self.people + 1

    def  capacity_is_full(self):
        ''' verifies the capacity of people with the number of routes '''
        if len(self.route) >= self.people :
            return True
        else:
            return False

    def show_all_variables(self):
        print(f'Status: {self.status}')
        print(f'Current Floor: {self.current_floor}°')
        print('Route:')
        for route in self.route:
            print(f'  Floor: {route["floor"]} || Total of People: {route["total"]}')
        is_opened = 'Open' if self.is_opened else 'Closed'
        print(f'Door: {is_opened}')
        print(f'Number of people: {self.people}')
        print(f'---------------------------- \n')

#  initial elevator status: on the ground floor, open doors, stopped, no people.
obj = Elevator()
obj.show_all_variables()

#  adds a user, with route to the fifth floor
obj.set_people()
obj.set_route(5)
obj.show_all_variables()

# add a new user who requests to go to the floor where the elevator is (ground floor) -
# Error test: Do not add another user to the total number of people
obj.set_people()
obj.set_route(0)
obj.show_all_variables()


# add a user who requests to go to a floor already requested (fifth) /
# Error test - counts an extra person in the elevator
obj.set_people()
obj.set_route(5)
obj.show_all_variables()

#  adds a user, with route to the sixth floor
obj.set_people()
obj.set_route(6)
obj.show_all_variables()

# moves the elevator up through the requested routes.
# When landing a user, decreases a route already made and decreases in the total number of people
obj.move()

# after doing the previous routes, add a new user user with route to the fourth floo
obj.set_people()
obj.set_route(4)
obj.show_all_variables()

# Error Handling: requesting two routes by a user
# adding just one person to each route
obj.set_people()
obj.set_route(2)
obj.set_route(1)
obj.show_all_variables()

# adds a new user, with new route to the first floor
obj.set_people()
obj.set_route(1)
obj.show_all_variables()


# move the elevator down until completing all the routes
# to the elevator, open the doors, and zero the number of routes and people.
obj.move()
obj.show_all_variables()
