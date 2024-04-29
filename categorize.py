import os

filename_list = list()

categories = {
    "success stories": ["success_stories", "success_story", "successstory", "successstories"],
    "case studies": ["case_study", "case_studies", "casestudy", "casestudies"],
    "brochures": ["brochure", "brochures"],
    "datasheets": ["datasheet", "datasheets"],
    "guides": ["guide", "guides"],
    "briefs": ["brief", "briefs"],
    "white papers": ["white_paper", "white_papers", "whitepaper", "whitepapers"],
    "misc": []
}

other = list()

category_counts = {category: 0 for category in categories}

def categorize_files(directory):
    for filename in os.listdir(directory):
        filename_list.append(filename)
        if os.path.isfile(os.path.join(directory, filename)):
            match = False
            for category, keywords in categories.items():
                for keyword in keywords:
                    if keyword.lower() in filename.lower():
                        category_counts[category] += 1
                        match = True
                        break
                if match is True:
                    break
            if match is False:
                category_counts["misc"] += 1
                other.append(filename)

directory_path = "file"

categorize_files(directory_path)

print(filename_list)
print(len(filename_list))

for category, count in category_counts.items():
    print(f"{category}: {count} files")

print(other)