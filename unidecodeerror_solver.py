import charset_normalizer
    
def encoding(path_to_file):
    
    """Takes path of the dataframe and returns dict with language and encoding used  """
    with open(path_to_file,'rb')as raw_data:
    
        output_dict = charset_normalizer.detect(raw_data.read())
        return output_dict['encoding']


if __name__ == "__main__":
    print("This will only run when the script is executed directly.")
