import db from "../../db/client.js"

export const saveToDatabase = (blog) => {
    // Save to database
        return db.Blog.create({
            data:blog
        });

}

export const getAllBlogs = async () => {
    try {
        const blogs = await db.Blog.findMany({
            orderBy: {
                date: 'desc',
            },
        });
        return blogs;
    } catch (error) {
        console.log(error);
        return [];
    }
};


export const getBlogById = async (blogId) => {
	return db.Blog.findFirstOrThrow({
		where: {
			id: blogId
		},
		select: {
            id:true,
			title:true,
            tags:true,
            content:true,
            date:true,
		}
	})
}

export const updateBlog = async (blogId,data) => {
	return db.Blog.update({
		where: {
			id: blogId
		},
        data:data,
		select: {
			title:true,
            tags:true,
            content:true,
            updatedAt:true,
		}
	})
}

export const deleteBlog= async (blogId)=>{
    return db.Blog.delete({
    where: {
      id: blogId
    },
  });
}
