import colourdescriptor
import searcher
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
cd = colourdescriptor.ColourDescriptor((8, 12 ,3))

# load query and get it's features
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform search
searcher = searcher.Searcher(args["index"])
results = searcher.search(features)

# display query
cv2.imshow("Query", query)

# loop over results
for (score, result_id) in results:
    result = cv2.imread(result_id)
    cv2.imshow("Result", result)
    cv2.waitKey(0)

