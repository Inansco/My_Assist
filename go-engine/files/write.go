package files

import "os"

func WriteFile(path string, content string) error {
	return os.WriteFile(path, []byte(content), 0644)
}