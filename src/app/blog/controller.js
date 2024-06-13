import {saveToDatabase} from './repository.js'
import { getAllBlogs } from './repository.js'

export const saveBlog = async (req, res) => {
    const { title, content, tags,date } = req.body;
    const blog = {
        title,
        tags,
        content,
        date
    };
    const result = await saveToDatabase(blog);
    if(result) {
        return res.send({
            status: 201,
            message: "blog saved successfully"
        });
    }
    else
    {
        return res.send({
            status: 500,
            message: "blog could not be saved"
        });
    }
}

export const getBlogs = async (req, res) => {
    try {
        const blogs = await getAllBlogs();
        if (blogs.length > 0) {
            return res.send({
                status: 200,
                data: blogs,
                message: "Blogs retrieved successfully"
            });
        } else {
            return res.send({
                status: 404,
                message: "No blogs found"
            });
        }
    } catch (error) {
        return res.send({
            status: 500,
            message: "An error occurred while retrieving blogs",
            error: error.message
        });
    }
};
