package files

type PathRequest struct {
	Path string `json:"path"`
}

type WriteRequest struct {
	Path    string `json:"path"`
	Content string `json:"content"`
}