(require 'ox-publish)
(setq org-publish-project-alist
      `(("notes"
	 :base-directory ,(expand-file-name "./notes/")
	 :publishing-directory ,(expand-file-name "./notes-html/")
	 :publishing-function org-html-publish-to-html
	 :with-toc nil
	)))

(defun add-tangle-info (backend)
  (let ((ref->file nil))
    (org-babel-map-src-blocks nil
      (let* ((args-alist (org-babel-parse-header-arguments header-args))
	     (tangle (alist-get ':tangle args-alist))
	     (noweb-ref (alist-get ':noweb-ref args-alist))
	     (noweb-file (and noweb-ref (alist-get noweb-ref ref->file nil nil 'string=))))
	(when (and (string= (alist-get ':noweb args-alist) "yes") tangle)
	  ;; only works for code blocks consisting solely of a single noweb-ref
	  (setq ref->file (cons
			   (cons (replace-regexp-in-string "[<>\n]" "" body) (format ">> %s" tangle))
			   ref->file)))
	(when (or tangle noweb-file)
	  (insert (format "#+CAPTION: =%s=\n" (or tangle noweb-file))))))))

(add-hook 'org-export-before-processing-hook 'add-tangle-info)
