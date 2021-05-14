# 다수의 List 컴포넌트의 가상화를 통한 빠른 렌더링
* 200개 정도 되는 Array를 각각의 컴포넌트로 렌더링하면, 아무리 컴퓨터 성능이 좋아도 Web Base에서 실행되는 한계로 인해 딜레이가 생길 수 밖에 없음.
* 이를 react-window를 사용하여 사용자의 눈에 보이는 것만 렌더링하는 방식으로 해결할 수 있음.
```tsx
{(() => {
                const filteredArray = foo[];
                return (
                  <FixedSizeList
                    height={200}
                    width={466}
                    itemSize={35}
                    itemCount={filteredArray.length}>
                    {({ index, style }) => {
                      const item = filteredArray[index];
                      return (
                        <ListItem
                          button
                          className={classes.listWrapper}
                          style={style}
                          key={`foobar`}>
                          <ListItemText
                            primary={<span>{item}</span>}
                          />
                        </ListItem>
                      );
                    }}
                  </FixedSizeList>
                );
              })()}
```
* 또한, 위 코드의 FixedSizeList의 인자로 들어가는 height, width는 부모의 Dynamic Size에 대비하여 추가적으로 `AutoSizer`을 도입할 수 있음.
```tsx
import AutoSizer from "react-virtualized-auto-sizer";
 <AutoSizer>
      {({ height, width }) => (
            <FixedSizeList
                  //...
```
