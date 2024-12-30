# # 1. Create a function that "predicts" whether or not a refund will be issued. Based on the valid and invalid refund requests in our sample set, we need to identify a set of parameters - in this case, boundaries - to create and train our model.

# # 2. Determine whether or not your model returns "good predictions" by comparing your the output of your function to the `training_data`. Adjust your boundaries as necessary to increase the accuracy of your training model.

# # 3. Validate your model by passing the `validation_data` as an argument to your training model function. Does your training function return accurate predictions?

training_data = [
    {
        "name": "Leilani",
        "amount": 500,
        "years": 0.1,
        "prior_requests": 10,
        "accounts_on_IP": 10,
        "refund": False,
    },
    {
        "name": "Niamh",
        "amount": 17,
        "years": 4,
        "prior_requests": 1,
        "accounts_on_IP": 1,
        "refund": True,
    },
    {
        "name": "Priya",
        "amount": 200,
        "years": 1,
        "prior_requests": 5,
        "accounts_on_IP": 2,
        "refund": True,
    },
    {
        "name": "Idris",
        "amount": 250,
        "years": 1,
        "prior_requests": 6,
        "accounts_on_IP": 1,
        "refund": True,
    },
    {
        "name": "Zara",
        "amount": 200,
        "years": 1,
        "prior_requests": 5,
        "accounts_on_IP": 2,
        "refund": True,
    },
    {
        "name": "Hiroshi",
        "amount": 400,
        "years": 4,
        "prior_requests": 2,
        "accounts_on_IP": 15,
        "refund": False,
    },
]

validation_data = [
    {
        "name": "Mei-Ling",
        "amount": 50,
        "years": 7,
        "prior_requests": 2,
        "accounts_on_IP": 1,
        "refund": True,
    },
    {
        "name": "Santiago",
        "amount": 100,
        "years": 2,
        "prior_requests": 1,
        "accounts_on_IP": 2,
        "refund": True,
    },
    {
        "name": "Aisha",
        "amount": 200,
        "years": 1,
        "prior_requests": 5,
        "accounts_on_IP": 10,
        "refund": False,
    },
    {
        "name": "Amara",
        "amount": 135,
        "years": 0.5,
        "prior_requests": 14,
        "accounts_on_IP": 2,
        "refund": False,
    },
]


def predict_refund(request):
    # Predict whether a refund should be issued based on heuristics derived from the data

    return not (
        request["amount"] > 400
        or request["years"] < 0.9
        or request["prior_requests"] > 10
        or request["accounts_on_IP"] > 9
    )


def get_model_accuracy(data):
    # Calculate the accuracy of the model on a given dataset

    # invoke your model for each request in data and compare its prediction to the actual refund status
    num_correct_predictions = sum(
        predict_refund(entry) == entry["refund"] for entry in data
    )

    # return the accuracy of your model
    return 100 * num_correct_predictions / len(data)


# # Train your model against (ONLY) the training data, tweaking as necessary to maximize its accuracy

# # Once you're happy with your model's accuracy, check it against the validation data!
# # How does your model fare against the validation data?

print("Training Data Accuracy:", get_model_accuracy(training_data))
print("Validation Data Accuracy:", get_model_accuracy(validation_data))
