def file_read_write():
    """
    Reads a file, modifies its content, and writes to a new file.
    Handles file not found and permission errors gracefully.
    """
    print("📂 File Modifier Program")
    print("-----------------------")
    
    # Get input filename with error handling
    while True:
        try:
            input_filename = input("Enter the filename to read: ")
            
            # Try opening the file
            with open(input_filename, 'r') as file:
                content = file.read()
                
            break  # Exit loop if file read successfully
            
        except FileNotFoundError:
            print(f"❌ Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"❌ Error: Permission denied when accessing '{input_filename}'. Try another file.")
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}. Please try again.")
    
    # Get output filename with validation
    while True:
        output_filename = input("Enter new filename to save modified content: ")
        
        if output_filename.strip() == "":
            print("❌ Error: Filename cannot be empty. Try again.")
        elif output_filename == input_filename:
            print("❌ Error: Output filename cannot be same as input. Try again.")
        else:
            break
    
    # Modify content (convert to uppercase in this example)
    modified_content = content.upper()
    
    # Write to new file with error handling
    try:
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"✅ Success! Modified content saved to '{output_filename}'")
        
    except PermissionError:
        print(f"❌ Error: Cannot write to '{output_filename}'. Permission denied.")
    except Exception as e:
        print(f"❌ Error saving file: {str(e)}")

# Run the program
if __name__ == "__main__":
    file_read_write()