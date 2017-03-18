# project/run.py

# Separating out concerns by:
# Remove unnecessary code from the controller that does not pertain to the actual business logic.


from views import app
app.run(debug=True)
