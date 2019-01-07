 vector<vector<int>> levelOrder(Node* root) {
	// if root is empty, then return
	if (nullptr == root) {
		return {};
	}

	// declare return value
	vector<vector<int>> Return;

	// declare nexet level node
	vector<Node*> NextLevelQueue;

	// insert node to queue
	vector<Node*> Vector{ {root} };

	// circulation until queue is empty
	while (!Vector.empty()) {
		// declare child value
		vector<int> ChildValue;

		for (const auto& VectorIndex : Vector) {
			// insert value
			ChildValue.push_back(VectorIndex->val);

			// insert child node, if possible
			for (const auto& NodeIndex : VectorIndex->children)
				NextLevelQueue.push_back(NodeIndex);
		}
		// insert key to return
		Return.push_back(ChildValue);
		Vector = std::move(NextLevelQueue);
	}
	return Return;
    }
