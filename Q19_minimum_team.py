# Q19. Minimum Team Selection to Cover Required Skills
# Select the minimum number of candidates to cover all required skills.

skills = ["Python", "SQL", "MachineLearning", "DataStructures"]

candidates = [
    ["Python", "SQL"],
    ["SQL", "MachineLearning"],
    ["MachineLearning", "DataStructures"],
    ["DataStructures"]
]

# Assign a unique bit position to each required skill.
skill_index = {}

for i in range(len(skills)):
    skill_index[skills[i]] = i

# Create a bitmask representing all required skills.
target = (1 << len(skills)) - 1

# Convert each candidate's skills into a bitmask.
candidate_masks = []

for candidate in candidates:

    mask = 0

    for skill in candidate:

        if skill in skill_index:
            mask |= (1 << skill_index[skill])

    candidate_masks.append(mask)

# Store the smallest team for every skill combination.
# Key = covered skills, Value = selected candidate indices.
dp = {0: []}

# Process every candidate.
for i in range(len(candidates)):

    new_dp = dp.copy()

    for mask, team in dp.items():

        # Add the current candidate's skills.
        new_mask = mask | candidate_masks[i]

        # Create a new team.
        new_team = team + [i]

        # Keep the smaller team for this combination.
        if new_mask not in new_dp or len(new_team) < len(new_dp[new_mask]):
            new_dp[new_mask] = new_team

    dp = new_dp

# Get the minimum team covering all required skills.
answer = dp[target]

print("Selected Team:", answer)