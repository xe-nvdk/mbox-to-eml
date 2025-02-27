import mailbox
import os
import sys

def mbox_to_eml(mbox_file, output_folder):
    """Convert an mbox file to separate .eml files."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mbox = mailbox.mbox(mbox_file)
    idx = 0  # Initialize idx before the loop

    for idx, message in enumerate(mbox):
        eml_file_path = os.path.join(output_folder, f"email_{idx+1}.eml")
        with open(eml_file_path, "w", encoding="utf-8") as eml_file:
            eml_file.write(message.as_string())

    print(f"Conversion completed! Saved {idx+1} emails to '{output_folder}'." if idx > 0 else "No emails found in the mbox file.")

# Example usage with command-line arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <mbox_file_path> <output_folder>")
        sys.exit(1)
    
    input_mbox = sys.argv[1]
    output_directory = sys.argv[2]
    mbox_to_eml(input_mbox, output_directory)
  
