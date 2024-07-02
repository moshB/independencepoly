from collections import defaultdict

def find_all_sums(nums, target_sum):
  """
  This function finds all unique combinations of numbers from a list that add up to a target sum.

  Args:
      nums: A list of integers.
      target_sum: The target sum to achieve.

  Returns:
      A list of lists, where each inner list represents a combination of numbers that add up to the target sum.
  """

  all_sums = []
  count_dict = defaultdict(int)  # Use a dictionary to store counts of each number

  for num in nums:
    count_dict[num] += 1

  def dfs(current_list, remaining_sum, start_index):
    """
    Performs a depth-first search to find all combinations.

    Args:
        current_list: A list containing the current combination of numbers.
        remaining_sum: The remaining sum to achieve after adding the current number.
        start_index: The index from which to start searching in the nums list (prevents duplicates).
    """
    # print(f"Current list: {current_list}, Remaining sum: {remaining_sum}, Count dict: {count_dict}")  # Print for debugging
    if remaining_sum == 0:
      if current_list in all_sums:
        return
      else:
        all_sums.append(current_list.copy())  # Append a copy to avoid modification
      return

    # Iterate through unique numbers from start_index
    for i in range(start_index, len(nums)):
      if nums[i] <= remaining_sum and count_dict[nums[i]] > 0:  # Check if remaining and count allows using the number
        current_list.append(nums[i])
        count_dict[nums[i]] -= 1
        dfs(current_list, remaining_sum - nums[i], i)  # Maintain start_index to avoid duplicates within a branch
        count_dict[nums[i]] += 1
        current_list.pop()

  dfs([], target_sum, 0)
  # Print the results here to check
  print(all_sums)
  return all_sums

# Example usage
# nums = [1,2,3, 4]
if __name__ == '__main__':


  nums = []
  target_sum = 2
  for i in range(1,target_sum+1):
    for j in range(target_sum//i+1):
      if i != 4:
        nums.append(i)

  all_possible_sums = find_all_sums(nums, target_sum)


