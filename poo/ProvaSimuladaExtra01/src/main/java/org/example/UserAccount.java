package org.example;

public class UserAccount {
    private final String email;
    private final String userName;

    private UserAccount[] blockedFollowers;
    private int numberOfBlockedF;
    private Post[] posts;
    private int numberOfPosts;
    private UserAccount[] followers;
    private int numberOfFollowers;
    private Post[] timeline;
    private int numberOfPostsTimeLine;

    public UserAccount(String userName, String email) {
        this.userName = userName;
        this.email = email;
        this.blockedFollowers = new UserAccount[50];
        this.timeline = new Post[10];
        this.posts = new Post[100];
        this.followers = new UserAccount[50];
        this.numberOfPosts = 0;
        this.numberOfFollowers = 0;
        this.numberOfPostsTimeLine = 0;
        this.numberOfBlockedF = 0;
    }

    public void publish(String quote){
        Post newPost = new Post(this,quote);
        posts[numberOfPosts] = newPost;
        numberOfPosts++;

        for (int i = 0; i < numberOfFollowers; i++) {
            followers[i].updateTimeLine(newPost);
        }
    }

    public boolean delete(int postIdx){
        if (postIdx < 0 || postIdx >= numberOfPosts) { return false; }

        for (int i = 0; i < numberOfPosts; i++) {
            if (postIdx == posts[i].getId()){
                for (int j = i; j < numberOfPosts - 1; j++) {
                    posts[j] = posts[j + 1];
                }
                posts[numberOfPosts - 1] = null;
                numberOfPosts--;
                return true;
            }
        }
        return false;
    }

    public String showTimeLine(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numberOfPostsTimeLine; i++) {
            sb.append(timeline[i].show()).append("\n");
        }
        return sb.toString();
    }

    public String showMyPosts(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numberOfPosts; i++) {
            sb.append(posts[i].show()).append("\n");
        }
        return sb.toString();
    }

    public String showMyFriends(){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numberOfFollowers; i++) {
            sb.append(followers[i].getUserName()).append("\n");
        }
        return sb.toString();
    }

    public void clapPost(int postIdx){
        if (postIdx >= 0 && postIdx < numberOfPostsTimeLine) {
            timeline[postIdx].clap();
        }
    }

    public void booPost(int postIdx){
        if (postIdx >= 0 && postIdx < numberOfPostsTimeLine) {
            timeline[postIdx].boo();
        }
    }

    public void updateTimeLine(Post post) {
        if (numberOfPostsTimeLine == 10) {
            for (int i = 1; i < 10; i++) {
                timeline[i - 1] = timeline[i];
            }
            timeline[9] = post;
        }
        else {
            timeline[numberOfPostsTimeLine++] = post;
        }
    }

    public void acceptFollower(UserAccount newFollower){
        boolean canAccept = true;
        for (int i = 0; i < numberOfBlockedF; i++) {
            if (blockedFollowers[i].getUserName().equals(newFollower.getUserName())) {
                canAccept = false;
            }
        }
        if (canAccept) followers[numberOfFollowers++] = newFollower;
    }

    public void blockAccount(UserAccount follower){
        blockedFollowers[numberOfBlockedF] = follower;
        for (int i = 0; i < numberOfFollowers; i++) {
            if (followers[i] == follower) {
                for (int j = i; j < numberOfFollowers - 1; j++) {
                    followers[j] = followers[j + 1];
                }
                followers[numberOfFollowers - 1] = null;
                numberOfFollowers--;
                break;
            }
        }
    }

    public String getUserName() {
        return userName;
    }
}
