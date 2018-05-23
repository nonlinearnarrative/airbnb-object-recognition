# Airbnb object recognition

Creates a collection of JSON files with recognized objects in photos of Airbnb listings.

## Obtaining the photos
Use our [scrape-airbnb](https://github.com/nonlinearnarrative/scrape-airbnb) tool. This will also pull in all other data about the listings. To run the object recognition on the photos, place them in a folder called `photos` with the following subfolders:
- `host-photos` containing the picture of the host of each listing, named `[listing-id].jpg`
- `listing-photos` containing subfolders for each listing, which in turn contain all photos of that listing, starting at `0.jpg`

## Running the script
We use [Darknet's Yolo](https://pjreddie.com/darknet/yolo/) for object recognition. To configure this, do the following:
```bash
# Download the darknet repo
git submodule update --init --recursive

# Compile the executable
cd darknet
make

# Download pre-trained weight file
wget https://pjreddie.com/media/files/yolov3.weights
```
Once Darknet is configured, you can run the script with:

```python
python recognition.py
```

## About this project
[`airbnb-object-recognition`](https://github.com/nonlinearnarrative/airbnb-object-recognition) and [`scrape-airbnb`](https://github.com/nonlinearnarrative/scrape-airbnb) were written as part of a workshop at [Non-Linear Narrative](https://www.kabk.nl/en/programmes/master/non-linear-narrative) at Royal Academy of Art The Hague. They are tools used to create [No Home Like Place](https://github.com/nonlinearnarrative/no-home-like-place).
