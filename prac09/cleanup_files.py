"""
Name: Sun Peishan
CP1404/CP5632 Practical - Suggested Solution
Cleanup inconsistent song lyrics file names
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename"""
    new_name = ""
    for i,current_letter in enumerate(filename,start=1):
        new_name += current_letter
        if i < len(filename):
            if current_letter.isalnum and filename[i].isupper():
                new_name += "_"
    print(new_name)

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name



if __name__ == '__main__':
    main()
