import {saveToDatabase} from './repository.js'

export const saveBlog = async (req, res) => {

    const content = req.body;
    const blog =content;
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

// const getBlogs = async (req, res) => {
//     const blogs = await Blog.findAll();
//     return res.json(blogs);
// }
