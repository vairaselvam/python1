import face_recognition
import pickle
import os
from PIL import Image
import numpy
import json

def get_face_embeddings_from_image(image, convert_to_rgb=False):
    if convert_to_rgb:
        image = image[:, :, ::-1]

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
   
    return face_locations, face_encodings

def face_train():
    from urllib import request
    import io
    database_filename = 'database.file'
    if os.path.exists(database_filename):
        with open(database_filename,'rb') as rfp: 
            database = pickle.load(rfp)

    response = request.urlopen("https://vairastorage.blob.core.windows.net/stylestore/250518060005?12/18/2018")
    # response = request.urlopen("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgolORTuMr7IGUnxT3j80TAvNA86K_PoFrGgaciICuJBwXGXa2")
    image_data = response.read()
    image_rgb = Image.open(io.BytesIO(image_data))
    image_numpy = numpy.asarray(image_rgb)
    identity = 'Vaira6'
    image_numpy = image_numpy[:,:,0:3]
    locations, encodings = get_face_embeddings_from_image(image_numpy)

    if len(encodings) == 0:
        print(f'Face encodings not found for user {identity}.')
    else:
        print(f'Encoding face for user: {identity}')
        database[identity] = encodings[0]

    with open(database_filename,'wb') as wfp:
        pickle.dump(database, wfp)

    return database.keys()

