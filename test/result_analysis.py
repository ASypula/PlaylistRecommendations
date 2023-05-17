from statistics import mean, median
from matplotlib import pyplot as plt

NR_USERS_POS = 5

def analyze_per_user_nr(results, model_name):
    all_values = []
    for key in results:
        all_values+=results[key]
    avg_model = mean(all_values)
    print(f"Average from {model_name}: {avg_model}")
    median_model = median(all_values)
    print(f"Median from {model_name}: {median_model}")
    return (avg_model, median_model, all_values)

def graphs_per_nr_users(results_model, results_random):
    fig, axes = plt.subplots(nrows=2, ncols=2)
    keys = list(results_model.keys())
    i=0
    for axis in axes.flatten():
        axis.hist([results_model[keys[i]], results_random[keys[i]]], label=['model', 'random'], color=['lightblue', 'navy'])
        axis.set_title(f"For {keys[i]} users")
        i+=1
    plt.legend(loc='upper right')
    plt.show()

def draw_graphs_for_all(all_results_model, all_results_random):
    plt.hist([all_results_model, all_results_random], label=['model', 'random'])
    plt.legend(loc='upper right')
    plt.show()

def analyze(file_model = "test_results_model.txt", file_random="test_results_random.txt"):
    model_results = load_data(file_model)
    random_results = load_data(file_random)
    model_avg, model_mean, model_all = analyze_per_user_nr(model_results, "model")
    random_avg, random_mean, random_all = analyze_per_user_nr(random_results, "model")
    # draw_graphs_for_all(model_all, random_all)
    graphs_per_nr_users(model_results, random_results)


def load_data(file):
    results = {}
    with open(file) as fp:
        for line in fp:
            nr = line.split(' ')[NR_USERS_POS]
            result = round(float(line.split(':')[-1]), 3)
            if nr in results.keys():
                results[nr].append(result)
            else:
                results[nr] = [result]
    return results


if __name__=="__main__":
    analyze()