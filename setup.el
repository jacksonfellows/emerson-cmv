(require 'ox-publish)
(setq org-publish-project-alist
      `(("notes"
	 :base-directory ,(expand-file-name "./notes/")
	 :publishing-directory ,(expand-file-name "./notes-html/")
	 :publishing-function org-html-publish-to-html
	 :with-toc nil
	)))
