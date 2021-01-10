import colourdescriptor
import searcher as Searcher
import argparse
import cv2

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
                help="Path to storage directory")
ap.add_argument("-q", "--query", required=True,
                help="Path to query directory")
ap.add_argument("-r", "--result-path", required=True,
                help="Path to results directory")
args = vars(ap.parse_args())

# initialize colour descriptor
cd = colourdescriptor((8, 12 ,3))

# load query and get it's features
query = cv2.imread(args["query"])
features = cd.describe()

# perform search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display query
cv2.imshow("Query", query)

# loop over results
for (score, results_id) in results:
    result = cv2.imread(args["result_path"] + "/" + results_id)
    cv2.imshow("Result", result)
    cv2.waitKey(0)

