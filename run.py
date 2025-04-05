import pathlib

from keras.api.utils import to_categorical
from loguru import logger
import numpy as np
from PIL import Image

from stamen import __ROOT__
from stamen.img import tile
from stamen.cnn import CNN

IMG_DIR = __ROOT__.joinpath('imgs')

data = []
labels = []

# 1. If any pics in 'training_input', read them in and train the model
p: pathlib.Path
for p in IMG_DIR.joinpath('training_input').rglob('*'):
    if p.suffix not in ['.jpg', '.png']:
        continue
    img = Image.open(p)
    img = img.resize((64, 64))
    img = np.array(img)
    data.append(img)
    labels.append(1 if p.parent.name == 'positive' else 0)

data = np.array(data)
# Normalize pixel values
data = data.astype('float32') / 255.0

labels = np.array(labels)
labels = to_categorical(labels)

# 2. Train the model using the training data
model = CNN.build_model_b()
model = CNN.compile_and_train_model(model=model, data=data, labels=labels)

# 3. If any new pics in 'raw', break them up into chunks and move to 'unseen'.
p: pathlib.Path
for p in IMG_DIR.joinpath('raw').iterdir():
    if p.suffix not in ['.jpg', '.png']:
        continue
    logger.debug(f'Importing raw picture file {p}...')
    try:
        tile(p)
    except Exception as e:
        logger.error(f'Exception on file: {p}. Skipping deletion.')
    else:
        logger.debug('Removing file after successful tiling')
        p.unlink()


# 4. Iterate through unseen photos, categorize



