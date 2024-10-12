"""initial migration2

Revision ID: 48792976429f
Revises: 548667b51428
Create Date: 2024-10-12 17:22:04.167893

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48792976429f'
down_revision = '548667b51428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('admins')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('role', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    op.drop_table('admin_user')
    # ### end Alembic commands ###
