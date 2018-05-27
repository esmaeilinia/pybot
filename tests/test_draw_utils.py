import time
import numpy as np

from pybot.geometry.rigid_transform import RigidTransform, Pose
import pybot.externals.draw_utils as draw_utils

if __name__ == "__main__":

    print('Reset')
    time.sleep(1)

    print('Create new sensor frame')
    draw_utils.publish_sensor_frame('new_frame', RigidTransform(tvec=[0,0,1]))

    poses = [RigidTransform.from_rpyxyz(np.pi/180 * 10*j, 0, 0, j * 1.0, 0, 0)
             for j in range(10)]
    draw_utils.publish_pose_list('poses', poses, frame_id='origin')
    draw_utils.publish_pose_list('poses_new_frame', poses, frame_id='new_frame')

    print('Create point cloud with colors')
    X = np.random.rand(1000, 3)
    C = np.hstack((np.random.rand(1000, 1), np.zeros((1000,2))))
    draw_utils.publish_cloud('cloud', X, c='b',
                             frame_id='new_frame', reset=True)
    draw_utils.publish_line_segments('lines', X[:-1], X[1:],
                                     c='y', frame_id='new_frame')
    time.sleep(2)

    print('Overwriting point cloud')
    X = np.random.rand(1000, 3) + np.float32([5, 0, 0])
    C = np.hstack((np.random.rand(1000, 1), np.zeros((1000,2))))
    draw_utils.publish_cloud('cloud', X, c='r',
                             frame_id='new_frame', reset=True)
    draw_utils.publish_line_segments('lines', X[:-1], X[1:],
                                     c='r', frame_id='new_frame')

    print('Create 3 poses with ids 0, 1, and 2')
    for j in range(5):
        time.sleep(0.1)
        p = Pose.from_rigid_transform(j, RigidTransform(tvec=[j,0,0]))
        draw_utils.publish_pose_list('poses', [p], frame_id='origin', reset=False)

    print('Publish cloud with respect to pose_id=3')
    draw_utils.publish_cloud('cloud', X, c='g', frame_id='poses',
                             reset=False, element_id=3)

    print('Update same pose with new transform')
    for j in range(4):
        time.sleep(1)
        p = Pose.from_rigid_transform(0, RigidTransform(tvec=[j,j,0]))
        draw_utils.publish_pose_list('poses', [p], frame_id='origin', reset=False)

    # Publish cloud with respect to pose 0
    Xs = [X + 3, X + 4, X + 6]
    ids = [0, 1, 2]
    draw_utils.publish_cloud('cloud_with_poses', Xs, c=[C, 'r', 'g'], frame_id='poses', element_id=ids)
    for j in range(3):
        time.sleep(1)
        p = Pose.from_rigid_transform(0, RigidTransform(tvec=[1,j,0]))
        draw_utils.publish_pose_list('poses', [p],
                                     frame_id='origin', reset=False)
