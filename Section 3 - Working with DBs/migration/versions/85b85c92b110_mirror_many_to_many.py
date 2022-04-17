"""mirror many to many

Revision ID: 85b85c92b110
Revises: ccb84bd3aad3
Create Date: 2022-04-17 21:10:46.790380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85b85c92b110'
down_revision = 'ccb84bd3aad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_books_reader_id', table_name='books')
    op.drop_constraint('books_reader_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'reader_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('reader_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('books_reader_id_fkey', 'books', 'readers', ['reader_id'], ['id'])
    op.create_index('ix_books_reader_id', 'books', ['reader_id'], unique=False)
    # ### end Alembic commands ###
