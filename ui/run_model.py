import streamlit as st
import torch
import os


# @st.cache(allow_output_mutation=True)
def load_model(file):
    model = torch.load(file)
    # model.eval()
    return model

def save_file_yaml(content, file):
    output_file = os.path.join('../data/demo', file)

    if os.path.exists(output_file):
        os.remove(output_file)
        print("File removed")

    with open(output_file, 'w') as outfile:
        outfile.write(content)
    print('File {} saved!'.format(file.split('.')[0]))

def main():
    import streamlit as st
    st.title("TEST MODEL")
    
    def get_data():
        chr_name = None
        list_chr = ["all", "chr21 small", "chr22", "chrX"]
        st.sidebar.header("Select data")
        data_source = st.sidebar.radio("Choose Data Source:", ("Use Existing Data", "Upload Data"))
        if data_source == "Use Existing Data":
            chr_name = st.selectbox('Select chromosome', list_chr)
            if chr_name == "all" :
                chr_name = "null" 
        elif data_source == "Upload Data":
            bam_file = st.file_uploader('Upload your model', type=["bam"])
            list_chr = ["all", "chr21 small", "chr22", "chrX"]
            if bam_file is not None:
                chr_name = st.selectbox('Select chromosome', list_chr)
        return chr_name
    
    #Get logging level
    logging_name = ['Info', 'Warnings', 'Errors']
    log_level = st.selectbox('Select log level', logging_name)
    # Get data
    chr_name = get_data()
    if chr_name is not None:
        # Dynamically generate paths based on chr_name
        chr_name = chr_name.replace(' ', '.')
        bam_path = f"../data/demo/inputs/{chr_name}.bam"
        fai_path = f"../data/demo/inputs/{chr_name}.fa.fai"
        first_name = chr_name.split('.')[0]

        # Get input data to yamlfile
        # yaml_content = f"bam: \"{bam_path}\"\n"
        # yaml_content += f"fai: \"{fai_path}\"\n"
        # yaml_content += f"chr_names: [\"{first_name}\"]\n"
        # yaml_content += f"log_level: \"{log_level}\"\n"
        # save_file_yaml(yaml_content, f"data_config.yaml")
        

    

    

    #Get model
    model_file = st.file_uploader('Upload your model', type=['h5', 'pkl', 'joblib', 'pickle', 'pt', 'pth'])
    if model_file is not None:
        model_pth = '../data/demo/models/' + model_file.name

        # Get input model data to yamlfile
        model_yaml_content = f"model_path: \"{model_pth}\"\n"
        model_yaml_content += f"n_cpus: 1\n" 
        
        # Save yaml file to data folder
        save_file_yaml(model_yaml_content, f"model_config.yaml")
        if os.path.exists(model_pth):
            # remove old file
            os.remove(model_pth)
        # # Save the uploaded file to the local machine
        with open(model_pth, 'wb') as f:
            f.write(model_file.getvalue())

        st.success('Model file has been saved to your local machine.')


    
    
    # Save to YAML file
    # dir_path = '../data/demo'



    st.write(f'You have selected {chr_name}')
    st.write(f'Logging level: {log_level}')
    # price=0
    # if st.button("Predict"):
    #     price=requests.post(url="http://127.0.0.1:8000/predict",data=json.dumps(input_data))
    #     price=price.json()
    #     p=price['prediction']
    #     st.success(f'The Price of the Car is {p} lacks')
    

if __name__=='__main__':
    main()