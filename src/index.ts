import { BreadthFirstSearch, Node } from "./bfs";

const tree: Record<string, Node> = {
  "10": {
    value: "10",
    leftNode: "4",
    rightNode: "17",
  },
  "4": {
    value: "4",
    leftNode: "1",
    rightNode: "9",
  },
  "17": {
    value: "17",
    leftNode: "12",
    rightNode: "18",
  },
  "1": {
    value: "1",
    leftNode: null,
    rightNode: null,
  },
  "9": {
    value: "9",
    leftNode: null,
    rightNode: null,
  },
  "12": {
    value: "12",
    leftNode: null,
    rightNode: null,
  },
  "18": {
    value: "18",
    leftNode: null,
    rightNode: null,
  },
};

BreadthFirstSearch(tree, tree[10], "12");