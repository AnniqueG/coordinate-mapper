import csv
import math

file_path = "C:/Users/ricke/UNI/csi3140/project/coordinates.csv"

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rgb = None

    def set_rgb(self, rgb):
        self.rgb = rgb

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

def read_points_from_csv(file_path):
    points = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip first line
        next(csv_reader)  # Skip second line
        for row in csv_reader:
            point_str = row[0].replace('POINT (', '').replace(')', '')
            coordinates = point_str.split()
            x = float(coordinates[0])
            y = float(coordinates[1])
            point = Point2D(x, y)
            points.append(point)
    return points

# Write points to a CSV file
def write_points_to_csv(points, file_path):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for point in points:
            rgb = point.rgb
            color_label = get_color_label(rgb)  # Get color label based on RGB value
            csv_writer.writerow([point.x, f"{rgb} {color_label}"])

def get_color_label(rgb):
    if rgb == (255, 0, 0):
        return "red"
    elif rgb == (255, 255, 0):
        return "yellow"
    else:
        return "green"

def label_points(points, distance_threshold, red_count_threshold):
    num_points = len(points)

    for i in range(num_points):
        close_points_count = 0

        for j in range(num_points):
            if i == j:
                continue

            distance = points[i].distance(points[j])
            if distance <= distance_threshold:
                close_points_count += 1

        if close_points_count >= red_count_threshold:
            points[i].set_rgb((255, 0, 0))  # Assign red color
            print("REDDDD")
        elif close_points_count >= red_count_threshold // 2:
            points[i].set_rgb((255, 255, 0))  # Assign yellow color
            print("YELLOWWWWWWWW")
        else:
            points[i].set_rgb((0, 255, 0))  # Assign green color

    return points

def main():
    points = read_points_from_csv(file_path)

    # Create two points
    point1 = Point2D(3, 4)
    point2 = Point2D(6, 8)

    # Calculate distance between two points
    distance = point1.distance(point2)
    print("Distance between point1 and point2:", distance)

    # Write points to a CSV file
    points.append(point1)
    points.append(point2)
    write_points_to_csv(points, 'new_points.csv')
    print("Points written to CSV.")

    # Label the points
    distance_threshold = 0.0001
    red_count_threshold = 6
    labeled_points = label_points(points, distance_threshold, red_count_threshold)

    # Write labeled points to CSV
    write_points_to_csv(labeled_points, 'labeled_points.csv')
    print("Labeled points written to CSV.")

# Execute the main function
if __name__ == '__main__':
    main()
