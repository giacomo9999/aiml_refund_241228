// 1. Create a function that "predicts" whether or not a refund will be issued. Based on the valid and invalid refund requests in our sample set, we need to identify a set of parameters - in this case, boundaries - to create and train our model.

// 2. Determine whether or not your model returns "good predictions" by comparing your the output of your function to the `training_data`. Adjust your boundaries as necessary to increase the accuracy of your training model.

// 3. Validate your model by passing the `validation_data` as an argument to your training model function. Does your training function return accurate predictions?

const training_data = [
    {
        name: 'Leilani',
        amount: 500,
        years: 0.1,
        prior_requests: 10,
        accounts_on_IP: 10,
        refund: false,
    },
    {
        name: 'Niamh',
        amount: 17,
        years: 4,
        prior_requests: 1,
        accounts_on_IP: 1,
        refund: true,
    },
    {
        name: 'Priya',
        amount: 200,
        years: 1,
        prior_requests: 5,
        accounts_on_IP: 2,
        refund: true,
    },
    {
        name: 'Idris',
        amount: 250,
        years: 1,
        prior_requests: 6,
        accounts_on_IP: 1,
        refund: true,
    },
    {
        name: 'Zara',
        amount: 200,
        years: 1,
        prior_requests: 5,
        accounts_on_IP: 2,
        refund: true,
    },
    {
        name: 'Hiroshi',
        amount: 400,
        years: 4,
        prior_requests: 2,
        accounts_on_IP: 15,
        refund: false,
    },
]

const validation_data = [
    {
        name: 'Mei-Ling',
        amount: 50,
        years: 7,
        prior_requests: 2,
        accounts_on_IP: 1,
        refund: true,
    },
    {
        name: 'Santiago',
        amount: 100,
        years: 2,
        prior_requests: 1,
        accounts_on_IP: 2,
        refund: true,
    },
    {
        name: 'Aisha',
        amount: 200,
        years: 1,
        prior_requests: 5,
        accounts_on_IP: 10,
        refund: false,
    },
    {
        name: 'Amara',
        amount: 135,
        years: 0.5,
        prior_requests: 14,
        accounts_on_IP: 2,
        refund: false,
    },
]

const predict_refund = (request) => {
    // Predict whether a refund should be issued based on heuristics derived from the data

    return !(
        request.amount > 400 ||
        request.years < 0.9 ||
        request.prior_requests > 10 ||
        request.accounts_on_IP > 9
    )
}

const get_model_accuracy = (data) => {
    // Calculate the accuracy of the model on a given dataset
    // # invoke your model for each request in data and compare its prediction to the actual refund status

    totalCorrect = data.filter((entry) => {
        return predict_refund(entry) === entry.refund
    })

    // return the accuracy of your model
    return (100 * totalCorrect.length) / data.length
}

// Train your model against (ONLY) the training data, tweaking as necessary to maximize its accuracy
// console.log('Training Data Accuracy:', get_model_accuracy(training_data))

// Once you're happy with your model's accuracy, check it against the validation data!
// How does your model fare against the validation data?
// console.log('Validation Data Accuracy:', get_model_accuracy(validation_data))

console.log(get_model_accuracy(training_data))
console.log(get_model_accuracy(validation_data))
