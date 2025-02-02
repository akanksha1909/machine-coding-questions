from flip_bit_system import FlipFitSystem

flipfit_system = FlipFitSystem()

flipfit_system.add_center(1, "Koramangala")
flipfit_system.add_center(2, "Bellandur")

flipfit_system.add_slot(1, 1, "06 AM - 07 AM", "Weights", 3)
flipfit_system.add_slot(1, 2, "07 AM - 08 AM", "Weights", 3)


user_id = flipfit_system.register_user("Akanksha", "akanksha@gmail.com", "123456789", "password")

flipfit_system.view_workouts_for_day("02-02-25")

flipfit_system.book_workout(user_id, 1, 1, "02-02-25")
flipfit_system.book_workout(user_id, 1, 1, "02-02-25")

flipfit_system.view_user_plan(user_id, "02-02-25")

