from sklearn.neighbors import KDTree

from load_datasets import load_dataset


superchargers = load_dataset('centroids.csv')
cars = load_dataset('coordinates.csv')
num_cars = float(len(cars))
cars_tree = KDTree(cars)


def get_cars_within_radius_of_supercharger(radius, count_only=False):
  return cars_tree.query_radius(superchargers, radius, count_only=count_only)


def get_num_cars_within_radius_of_any_supercharger(radius):
  cars_within_radius_of_each_supercharger = get_cars_within_radius_of_supercharger(radius)
  cars_within_radius_of_any_supercharger = set()
  for nearby_cars in cars_within_radius_of_each_supercharger:
    cars_within_radius_of_any_supercharger = cars_within_radius_of_any_supercharger | set(nearby_cars)

  return len(cars_within_radius_of_any_supercharger)


def get_min_radius_with_n_percent_coverage(expected_coverage):
  min_radius = 0
  max_radius = 1
  coverage = get_num_cars_within_radius_of_any_supercharger(max_radius) / num_cars

  # Find upper and lower bounds on the radius.
  while coverage < expected_coverage:
    min_radius = max_radius
    max_radius *= 2
    coverage = get_num_cars_within_radius_of_any_supercharger(max_radius) / num_cars

  # Binary search for the minimum radius with the desired coverage.
  while min_radius < max_radius:
    radius = (max_radius + min_radius) // 2
    coverage = get_num_cars_within_radius_of_any_supercharger(radius) / num_cars
    if coverage < expected_coverage:
      min_radius = radius + 1
    elif coverage > expected_coverage:
      max_radius = radius

  return min_radius


def get_max_radius_with_at_most_n_cars_covered_per_supercharger(n):
  min_radius = 0
  max_radius = 1
  covered_cars = get_cars_within_radius_of_supercharger(max_radius, count_only=True)
  all_at_most_n = (
    lambda lst: all([x <= n for x in lst])
  )

  # Find upper and lower bounds on the radius.
  while all_at_most_n(covered_cars):
    min_radius = max_radius
    max_radius *= 2
    covered_cars = get_cars_within_radius_of_supercharger(max_radius, count_only=True)

  # Binary search for the maximum radius satisfying the given conditions.
  while min_radius < max_radius:
    radius = (max_radius + min_radius) // 2
    covered_cars = get_cars_within_radius_of_supercharger(radius, count_only=True)
    if all_at_most_n(covered_cars):
      min_radius = radius + 1
    else:
      max_radius = radius

  return radius


num_cars_within_5_meters = get_num_cars_within_radius_of_any_supercharger(5)
print('\nCars within 5 meters: {}'.format(num_cars_within_5_meters))

num_cars_within_10_meters = get_num_cars_within_radius_of_any_supercharger(10)
print('\nCars within 10 meters: {}'.format(num_cars_within_10_meters))

min_radius_with_80_percent_coverage = get_min_radius_with_n_percent_coverage(0.8)
print('\nMinimum radius with 80%% coverage: {}m'.format(min_radius_with_80_percent_coverage))

max_radius_with_at_most_1000_cars_covered_per_supercharger = get_max_radius_with_at_most_n_cars_covered_per_supercharger(1000)
print('\nMaximum radius with at most 1000 cars covered by each supercharger: {}m'.format(max_radius_with_at_most_1000_cars_covered_per_supercharger))
