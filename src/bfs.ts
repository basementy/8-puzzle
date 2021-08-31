export interface Node {
  value: string;
  leftNode: string | null;
  rightNode: string | null;
}

export const BreadthFirstSearch = (tree: Record<string, Node>, rootNode: Node, searchValue: string) => {
  let nodeQueue: Node[] = [];

  nodeQueue.push(rootNode);

  while (nodeQueue.length > 0) {
    let currentNode = nodeQueue[0];

    if (currentNode.value === searchValue) {
      console.log(`Current node is: ${currentNode.value} (Found it!)`);
      return;
    }

    if (currentNode.leftNode !== null) {
      nodeQueue.push(tree[currentNode.leftNode]);
    }

    if (currentNode.rightNode !== null) {
      nodeQueue.push(tree[currentNode.rightNode]);
    }

    console.log(`Current node is: ${currentNode.value}`);

    nodeQueue.shift();
  }

  console.log("Sorry, no such node found :(");
}