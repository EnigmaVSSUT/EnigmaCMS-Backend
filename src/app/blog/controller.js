import {saveToDatabase} from './repository.js'

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

// const getBlogs = async (req, res) => {
//     const blogs = await Blog.findAll();
//     return res.json(blogs);
// }