package files

import "os"

func CreateFolder(path string) error {
	return os.MkdirAll(path, 0755)
}

func CreateFile(path string) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}
	defer file.Close()

	return nil
}