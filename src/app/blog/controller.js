import { saveToDatabase } from "./repository.js";
import { getAllBlogs, getBlogById, updateBlog, deleteBlog } from "./repository.js";

/**
 * @type {import("express").RequestHandler}
 */
export const saveBlogController = async (req, res, next) => {
  const { title, content, tags, date } = req.body;
  const blog = {
    title,
    tags,
    content,
    date,
  };
  const result = await saveToDatabase(blog);
  if (result) {
    return res.send({
      status: 201,
      message: "blog saved successfully",
    });
  } else {
    return res.send({
      status: 500,
      message: "blog could not be saved",
    });
  }
};

/**
 * @type {import("express").RequestHandler}
 */
export const getBlogsController = async (req, res, next) => {
  try {
    const blogs = await getAllBlogs();
    if (blogs.length > 0) {
      return res.send({
        status: 200,
        data: blogs,
        message: "Blogs retrieved successfully",
      });
    } else {
      return res.send({
        status: 404,
        message: "No blogs found",
      });
    }
  } catch (error) {
    return res.send({
      status: 500,
      message: "An error occurred while retrieving blogs",
      error: error.message,
    });
  }
};

/**
 * @type {import("express").RequestHandler}
 */
export const getParticularBlogController = async (req, res, next) => {
  try {
    const { blogId } = req.params;
    const blog = await getBlogById(blogId);
    if (blog) {
      return res.send({
        status: 200,
        data: blog,
        message: "Blog retrieved successfully",
      });
    } else {
      return res.send({
        status: 404,
        message: "No blog found",
      });
    }
  } catch (error) {
    return res.send({
      status: 500,
      message: "An error occurred while retrieving blog",
      error: error.message,
    });
  }
};

/**
 * @type {import("express").RequestHandler}
 */
export const updateBlogController = async (req, res, next) => {
  try {
    let data = req.body;
    const updatedBlog = await updateBlog(data.id, data);
    
    if (updatedBlog) {
      return res.status(200).send({
        status: 200,
        data: updatedBlog,
        message: "Blog updated successfully",
      });
    } else {
      return res.status(404).send({
        status: 404,
        message: "Blog not found or update unsuccessful",
      });
    }
  } catch (error) {
    return res.status(500).send({
      status: 500,
      message: "An error occurred while updating the blog",
      error: error.message,
    });
  }
};

/**
 * @type {import("express").RequestHandler}
 */
export const deleteBlogController = async (req, res, next) => {
  try {
    const blogId = req.params.blogId;
    const deletionResult = await deleteBlog(blogId);

    if (deletionResult) {
      return res.status(200).send({
        status: 200,
        message: "Blog deleted successfully",
      });
    } else {
      return res.status(404).send({
        status: 404,
        message: "Blog not found or already deleted",
      });
    }
  } catch (error) {
    return res.status(500).send({
      status: 500,
      message: "An error occurred while deleting the blog",
      error: error.message,
    });
  }
};

