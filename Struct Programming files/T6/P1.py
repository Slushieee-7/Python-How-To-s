class ProjectDetails:
    def __init__(self, id, title, size, priority):
        self.id = int(id)
        self.title = title
        self.size = int(size)
        self.priority = int(priority)

    def to_line(self):
        return f"{self.id},{self.title},{self.size},{self.priority}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        if len(parts) == 4:
            return ProjectDetails(parts[0], parts[1], parts[2], parts[3])
        else:
            return None

class ProjectManager:
    def __init__(self, projects_file='projects.txt', completed_file='completed_projects.txt'):
        self.projects_file = projects_file
        self.completed_file = completed_file
        self.projects = []
        self.load_projects()
        self.schedule = []

    def load_projects(self):
        self.projects = []
        try:
            with open(self.projects_file, 'r') as file:
                for line in file:
                    project = ProjectDetails.from_line(line)
                    if project:
                        self.projects.append(project)
        except FileNotFoundError:
            # File doesn't exist yet, so no projects loaded
            pass

    def save_project(self, project):
        with open(self.projects_file, 'a') as file:
            file.write(project.to_line())
        self.projects.append(project)

    def view_project(self, id):
        id = int(id)
        for project in self.projects:
            if project.id == id:
                return project
        return None

    def view_all_projects(self):
        return self.projects

    def view_completed_projects(self):
        completed = []
        try:
            with open(self.completed_file, 'r') as file:
                for line in file:
                    completed.append(line.strip())
        except FileNotFoundError:
            pass
        return completed

    def create_schedule(self):
        # Schedule sorted by priority, then size ascending
        self.schedule = sorted(self.projects, key=lambda p: (p.priority, p.size))
        print("Schedule created successfully.")

    def view_schedule(self):
        if not self.schedule:
            print("Schedule not created yet. Please create a schedule first.")
            return []
        return self.schedule

    def get_next_project(self):
        if self.schedule:
            project = self.schedule.pop(0)  # pop front
            with open(self.completed_file, 'a') as file:
                file.write(project.to_line())
            # Remove from projects list as well
            self.projects = [p for p in self.projects if p.id != project.id]
            # Rewrite the projects file after removal
            with open(self.projects_file, 'w') as file:
                for p in self.projects:
                    file.write(p.to_line())
            return project
        else:
            return None

def main():
    manager = ProjectManager()

    while True:
        print("\n\t\t Menu \n")
        print("1. Input Project Details")
        print("2. View Projects")
        print("3. Scheduled Projects")
        print("4. Get a Project")
        print("5. Exit\n")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("\n--- Input Project Details ---")
            try:
                id = int(input("Enter Project ID (integer): "))
                title = input("Enter Project Title: ").strip()
                size = int(input("Enter Number of Pages (integer): "))
                priority = int(input("Enter Project Priority (lower number is higher priority): "))
                project = ProjectDetails(id, title, size, priority)
                manager.save_project(project)
                print("Project details saved successfully.")
            except ValueError:
                print("Invalid input! Please enter integer values for ID, size, and priority.")
        elif choice == '2':
            print("\nView Projects:")
            print("1. One Project")
            print("2. Completed Projects")
            print("3. All Projects")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                id = input("Enter Project ID to search: ")
                if id.isdigit():
                    project = manager.view_project(id)
                    if project:
                        print(f"Project ID: {project.id}")
                        print(f"Title: {project.title}")
                        print(f"Size (pages): {project.size}")
                        print(f"Priority: {project.priority}")
                    else:
                        print("Project not found with that ID.")
                else:
                    print("Invalid ID! Must be an integer.")
            elif sub_choice == '2':
                print("\nCompleted Projects:")
                completed = manager.view_completed_projects()
                if completed:
                    for proj in completed:
                        print(proj.strip())
                else:
                    print("No projects have been completed yet.")
            elif sub_choice == '3':
                all_projects = manager.view_all_projects()
                if all_projects:
                    print("\nAll Projects:")
                    for p in all_projects:
                        print(f"ID: {p.id}, Title: {p.title}, Size: {p.size}, Priority: {p.priority}")
                else:
                    print("There are no projects to display.")
            else:
                print("Invalid choice.")
        elif choice == '3':
            print("\nScheduled Projects:")
            print("1. Create Schedule")
            print("2. View Schedule")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                manager.create_schedule()
            elif sub_choice == '2':
                schedule = manager.view_schedule()
                if schedule:
                    print("\nSchedule (sorted by priority and size):")
                    for p in schedule:
                        print(f"ID: {p.id}, Title: {p.title}, Size: {p.size}, Priority: {p.priority}")
            else:
                print("Invalid choice.")
        elif choice == '4':
            project = manager.get_next_project()
            if project:
                print("\nTopmost project removed from schedule:")
                print(f"ID: {project.id}, Title: {project.title}, Size: {project.size}, Priority: {project.priority}")
            else:
                print("No projects in the schedule or schedule not created.")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
