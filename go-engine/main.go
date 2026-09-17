package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"Inansco-engine/apps"
	"Inansco-engine/files"
)

type AppRequest struct {
	Name string `json:"name"`
}

func health(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Inansco Engine Online")
}

// --------------------
// Applications
// --------------------

func openApp(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req AppRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := apps.Open(req.Name); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte("Opened"))
}

func closeApp(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req AppRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := apps.Close(req.Name); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte("Closed"))
}

// --------------------
// Files
// --------------------

func createFolder(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req files.PathRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := files.CreateFolder(req.Path); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte("Folder created"))
}

func createFile(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req files.PathRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := files.CreateFile(req.Path); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte("File created"))
}

func writeFile(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req files.WriteRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	if err := files.WriteFile(req.Path, req.Content); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte("File written"))
}

func readFile(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "POST only", http.StatusMethodNotAllowed)
		return
	}

	var req files.PathRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	content, err := files.ReadFile(req.Path)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Write([]byte(content))
}

func main() {

	http.HandleFunc("/health", health)

	http.HandleFunc("/apps/open", openApp)
	http.HandleFunc("/apps/close", closeApp)

	http.HandleFunc("/files/create-folder", createFolder)
	http.HandleFunc("/files/create-file", createFile)
	http.HandleFunc("/files/write", writeFile)
	http.HandleFunc("/files/read", readFile)

	fmt.Println("Inansco Engine running on :8081")

	err := http.ListenAndServe(":8081", nil)

	if err != nil {
		panic(err)
	}
}