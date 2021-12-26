from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/content/drive/MyDrive/Caption_data/label_Uit-ivc/dataset_uitviic_w2v.json',
                       image_folder='/content/drive/MyDrive/Caption_data/Uitviic_images/UIT-ViIC',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/content/drive/MyDrive/Models/a-PyTorch-Tutorial-to-Image-Captioning/OUTPUT_W2vuit',
                       max_len=50)
